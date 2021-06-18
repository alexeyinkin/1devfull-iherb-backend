const ALREADY_EXISTS = 6;

const functions = require('firebase-functions');
const tools = require('firebase-tools');
const admin = require('firebase-admin');

exports.isDuplicateEvent = async function (context) {
    let key = context.eventId + '_' + context.eventType;

    try {
        await admin
            .firestore()
            .doc(`processedEvents/${key}`)
            .create({ createdAt: admin.firestore.FieldValue.serverTimestamp() });
    } catch (error) {
        if (error.code !== ALREADY_EXISTS) {
            throw error;
        }
        functions.logger.debug('Duplicated event trigger!');
        return true;
    }

    await cleanupMaybe();
    return false;
};

async function cleanupMaybe() {
    if (Math.random() < 1.0 / 300) {
        await cleanup();
    }
}

async function cleanup() {
    const limitDate = new Date(Date.now() - 1000 * 60 * 10); // 10 minutes before now.

    const batch = admin.firestore().batch();

    const pastEvents = await admin
        .firestore()
        .collection('processedEvents')
        .orderBy('createdAt', 'asc')
        .where('createdAt', '<', limitDate)
        .limit(400)
        .get();

    pastEvents.forEach(event => batch.delete(event.ref));

    await batch.commit();
}

exports.incrementCounter = async function (path, fieldName, increment) {
    let target = admin.firestore();

    for (const pair of path) {
        target = target.collection(pair[0]).doc(pair[1]);
    }

    let fields = {};
    fields[fieldName] = admin.firestore.FieldValue.increment(increment);

    return target.update(fields);
};

exports.createIfExists = async function (existingPath, creationPath, set) {
    const documentRef = await admin
        .firestore()
        .doc(existingPath)
        .get();

    if (!documentRef.exists) return;

    set = set || {};
    set['createdAt'] = admin.firestore.FieldValue.serverTimestamp();

    try {
        await admin
            .firestore()
            .doc(existingPath + '/' + creationPath)
            .create(set);
    } catch (error) {
        if (error.code !== ALREADY_EXISTS) {
            throw error;
        }
    }
};

exports.deleteIfExists = async function (path) {
    try {
        await admin
            .firestore()
            .doc(path)
            .delete();
    } catch (error) {
        return false;
    }
    return true;
};

exports.deleteRecursive = async function (path) {
    await tools.firestore
        .delete(
            path,
            {
                project: process.env.GCLOUD_PROJECT,
                recursive: true,
                yes: true,
            },
        );
};

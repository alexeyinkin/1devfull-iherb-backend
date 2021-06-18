const functions = require('firebase-functions');
const admin = require('firebase-admin');
const counters = require('./counters.js');
const search = require('./search.js');
const util = require('./util.js');

const listenPath = '/conditions/{id}';
const minTitleIndexLength = 2;

exports.onCreate = functions.firestore.document(listenPath).onCreate(async (change, context) => {
    if (await counters.isDuplicateEvent(context)) {
        return null;
    }

    await exports.updateDerivedFields(context.params.id);
    return null;
});

exports.onUpdate = functions.firestore.document(listenPath).onUpdate(async (change, context) => {
    if (await counters.isDuplicateEvent(context)) {
        return null;
    }

    await exports.updateDerivedFields(context.params.id);
    return null;
});

exports.updateDerivedFields = async function (id) {
    let strings = [];

    const doc = await admin
        .firestore()
        .doc(`conditions/${id}`)
        .get();

    const map = doc.data();
    if (!map) {
        functions.logger.info('Condition not found: ' + id);
        return;
    }
    strings = strings.concat(util.initialSubstrings(map['title'], minTitleIndexLength));

    const keywords = search.stringsToSearchTerms(strings, minTitleIndexLength);

    const set = {
        keywords: keywords,
    };

    await admin
        .firestore()
        .doc(`conditions/${id}`)
        .update(set);
};

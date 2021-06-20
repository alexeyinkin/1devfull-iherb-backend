const admin = require('firebase-admin');
admin.initializeApp();

const conditions = require('./conditions.js');
exports.conditions_onCreate = conditions.onCreate;
exports.conditions_onUpdate = conditions.onUpdate;

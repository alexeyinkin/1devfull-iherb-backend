blacklist = {
    'him': 1,
    'she': 1,
    'the': 1,
    'they': 1,
};

exports.stringsToSearchTerms = function (strings, minLength) {
    let all = [];

    for (const str of strings) {
        if (!str) continue;
        all = all.concat(stringToSearchTerms(str));
    }

    const unique = [...new Set(all)];
    const allowed = [];

    for (const one of unique) {
        if (one.length < minLength) continue;
        if (one in blacklist) continue;
        allowed.push(one);
    }

    return allowed;
};

function stringToSearchTerms(string) {
    return string.trim().toLowerCase().split(/\s+/);
}

exports.initialSubstrings = function (str, startingAtLength) {
    if (!str) return [];

    const result = [str];

    for (let length = str.length; --length >= startingAtLength; ) {
        result.push(str.substr(0, length));
    }

    return result;
};

exports.initialSubstringsOfArray = function (arr, startingAtLength) {
    let result = [];

    for (const str of arr) {
        result = result.concat(exports.initialSubstrings(str, startingAtLength));
    }

    return result;
};

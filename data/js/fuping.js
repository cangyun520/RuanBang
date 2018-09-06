
function fuping() {
    var time = Date.now().toString();
    var encrypted = CryptoJS.AES.encrypt(CryptoJS.enc.Utf8.parse(Rb.Utility.JsonHelper.toJson({ code: "0KU4PRXX007REPVJHK44", password: "0KU4PRXX2Q80JPVJ", tenantId: "0KU0S8N54X0ASRHG8K89" }))
    , CryptoJS.enc.Utf8.parse(jEvent.data.key)
    , {
        iv: CryptoJS.enc.Utf8.parse((time + "000000000000000").substr(0, 16))
        , mode: CryptoJS.mode.CBC
        , padding: CryptoJS.pad.Pkcs7
    });
    var result = CryptoJS.enc.Utf8.parse(CryptoJS.enc.Base64.stringify(CryptoJS.enc.Utf8.parse(time)) + "," + encrypted.ciphertext.toString());
    var data = CryptoJS.enc.Base64.stringify(result);
    return data;
}

const CryptoJS = require('crypto-js')

var key = CryptoJS.enc.Utf8.parse("azp53h0kft7qi78q");
var iv = CryptoJS.enc.Utf8.parse("1g3qqdh4jvbskb9x");

function AES_Encrypt(word) {
    var srcs = CryptoJS.enc.Utf8.parse(word);
    var encrypted = CryptoJS.AES.encrypt(srcs, key, {
        iv: iv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    return encrypted.toString();
}

function AES_Decrypt(word) {
    var srcs = word;
    var decrypt = CryptoJS.AES.decrypt(srcs, key, {
        iv: iv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    return decrypt.toString(CryptoJS.enc.Utf8);
}

data = {
  "ccCourseId": 1000008950,
  "chapterId": 1000088196,
  "isApply": 1,
  "lessonId": 1000217178,
  "recruitId": 165501,
  "videoId": 12024525,
  "dateFormate": 1680585632000
}
saveDatabaseIntervalTimeV2 = "70OP22nZsTuLdUJd11tjJnXAHqhDa7dxOa1CH/1DPvXTjz776n+ekhC86TLf03Qo6E7N9lYYJ90iGb6zLA1tRjRD/uTyL+t/GGFhbAe8b+YAsIcBoputJQggDKfVEMiVTlOwlf+DX8YI0eszeXtBfZhmdw0XW17pY7//xysmPdB4bUhMwa9jTo3DVLq4zOeiWhXh5qz7Ijtl/KxH8k8LIFnFyG05duLFG0JrWz8sZWXWxKyESzupnaRKRFZoEGo7T3bTHDTauFwBgzhOxMrtoxPWk1FyMVCFvx9agPVDPuD/Z2SlVt27Vq9oRV7NdeujkV93oMZ5pohb3240aND1XQxcRBfTIieVe14bcu3MF6maBmVsjw5svlaxF1sOgQcbr9AisGzS5GAnxlkaY85fnBJSpvIdn7EvPhNamSNsKiN2aUe2mu+S2uIY2ZvW36wT"

saveCacheIntervalTimeV2 ="otOD5jBHt065Em13urihcxAhzPKvdMgouizcVLSw8CChpDzWDqWgsE3xRU10c9SrqPJp3z9CpMfsTwaKVjSam+tmpaYSaxWcq1zgwW28gG5vgy/U4TWDFFiEIbtF9lYcw7wJ4Z9odZzVJBx8bOPUDjY2NdwOEV9f429JoCihoNOI8l+xBQ3AsipChVorCiB0zooxkDrMcMWfx6nprdsosX5LTCD7Fin2mYPdHfRoru8fV1rjj/MMa3sa2h2sLGoufsfaMZp9cJQu8sLasoOnnq/UzakDnS+n/QegnzgaZ1pDXuYDkc7RB5FTpK/2yVN8flP1cPtbo7i9Ywy5LMUXqX6/xL7TMXvksogMvlPzouAh9rbQD7HTbL+NpIE85ViB2osoJgoGj8YAH5KJ5dXpG1phBzxdXiohTSI9b4tK2rIKADydZQ6IPIW+/9WmlFaldVNeREuXUEDWUDSWSMP07HCyuwlQpi3qbzwLlVZ7jMJgee7NuQ7NhgAIVNoicpNMc9nsxzkqobqUpoJSNwEN5VuvpSmRF6sf+iHjkBc/2WzYBKB9T1F3BqfkvPx0XaHJ"
data = "hwtr3Z4h8uz3aQth3mwLivDZwGSbRvgigk4Nqr1a6YcmL3Vpn+vcgK/9fmBj1WvpP/TCHVgcp0UD8WFtm+gqFA=="

zhuye = "NEuH3llD9woD4DQgu0k6Uvp5yyo8WT84Dq5lU2iPwvgKNatePzJ+vu/4PRaNYy+K"
// console.log(AES_Encrypt(data));
//
console.log(AES_Decrypt(data));

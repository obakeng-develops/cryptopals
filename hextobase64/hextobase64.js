// Always operate on raw bytes, never on encoded strings.
// CryptoPals 
// Obakeng Mosadi, 2022

s = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

function hexToBytes(hex) {

    let bytes = []

    try {
        for (c = 0; c < hex.length; c += 2) {
            bytes.push(parseInt(hex.substr(c, 2), 16));
        }

        let decodedByteArray = String.fromCharCode(...bytes)

        let b64_value = btoa(decodedByteArray)

        console.log(b64_value)
    } catch {
        console.log("Could not convert to base 64.")
    }

}

hexToBytes(s)
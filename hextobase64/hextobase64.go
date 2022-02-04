package main

import (
	"encoding/base64"
	"encoding/hex"
	"fmt"
)

func main() {

	s := "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

	decodedByteArray, err := hex.DecodeString(s)

	b64_value := base64.StdEncoding.EncodeToString(decodedByteArray)

	if err != nil {
		fmt.Println("Unable to convert hex to byte. ", err)
	}

	fmt.Printf("%s\n", decodedByteArray)
	fmt.Println(b64_value)
}

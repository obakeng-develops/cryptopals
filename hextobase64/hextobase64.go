package main

import (
	"encoding/base64"
	"fmt"
)

func main() {

	hex := "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

	base64_value := base64.StdEncoding.EncodeToString([]byte(hex))
	fmt.Println(base64_value)
}

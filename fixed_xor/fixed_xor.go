package main

import (
	"fmt"
	"strconv"
)

func strToBinary(s string, base int) []byte {

	var b []byte

	for _, c := range s {
		b = strconv.AppendInt(b, int64(c), base)
	}

	return b

}

func main() {

	binValueOne := strToBinary("1c0111001f010100061a024b53535009181c", 16)
	// binValueTwo := binary("686974207468652062756c6c277320657965")

	fmt.Println(binValueOne)

}

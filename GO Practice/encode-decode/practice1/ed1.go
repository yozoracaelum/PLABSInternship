package main

import (
	"encoding/base64"
	"fmt"
)

func main() {
	var data = "Eizen Stelidz"

	var encodedString = base64.StdEncoding.EncodeToString([]byte(data))
	fmt.Println("encoded: ", encodedString)

	var decodedByte, _ = base64.StdEncoding.DecodeString(encodedString)
	var decodedString = string(decodedByte)
	fmt.Println("decoded: ", decodedString)
}

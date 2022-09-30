package main

import (
	"crypto/sha1"
	"fmt"
)

func main() {
	var text = "This is secret"
	fmt.Println("Original: ", text)
	var sha = sha1.New()
	sha.Write([]byte(text))
	var encrypted = sha.Sum(nil)
	var encryptedString = fmt.Sprintf("%x", encrypted)

	fmt.Println("Hashed: ", encryptedString)
}

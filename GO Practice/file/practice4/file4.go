package main

import (
	"fmt"
	"os"
)

var path = "C:/Users/user/Documents/coba.txt"

func isError(err error) bool {
	if err != nil {
		fmt.Println(err.Error())
	}

	return (err != nil)
}

func deleteFile() {
	var err = os.Remove(path)
	if isError(err) {
		return
	}
	fmt.Println("==> file berhasil didelete")
}

func main() {
	deleteFile()
}

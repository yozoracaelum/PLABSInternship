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

func writeFile() {
	var file, err = os.OpenFile(path, os.O_RDWR, 0644)
	if isError(err) {
		return
	}
	defer file.Close()

	_, err = file.WriteString("Halo\n")
	if isError(err) {
		return
	}
	_, err = file.WriteString("Mari belajar golang\n")
	if isError(err) {
		return
	}

	err = file.Sync()
	if isError(err) {
		return
	}

	fmt.Println("==> file berhasil di isi")
}

func main() {
	writeFile()
}

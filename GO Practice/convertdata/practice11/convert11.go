package main

import "fmt"

func main() {
	var text1 = "Hello"
	var b = []byte(text1)
	var byte1 = []byte{72, 101, 108, 108, 111}
	var s = string(byte1)
	var c int64 = int64('h')
	var d string = string(104)

	fmt.Println(c)
	fmt.Println(d)
	fmt.Printf("%d %d %d %d \n", b[0], b[1], b[2], b[3])
	fmt.Printf("%s \n", s)
}

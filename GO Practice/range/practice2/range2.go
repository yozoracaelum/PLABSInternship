package main

import "fmt"

func main() {
	x := "hello"
	for _, c := range x {
		fmt.Println(c)
		fmt.Printf("%c\n", c)
	}
}

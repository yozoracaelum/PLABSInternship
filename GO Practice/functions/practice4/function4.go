package main

import "fmt"

func repeat(a string, b int) {
	for i := 0; i < b; i++ {
		fmt.Println(a)
	}
}

func main() {
	var w string
	fmt.Scanln(&w)
	var x int
	fmt.Scanln(&x)

	repeat(w, x)
}

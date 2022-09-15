package main

import "fmt"

func main() {
	x := 42
	p := &x

	*p = 8
	fmt.Println(*p)
	fmt.Println(x)
}

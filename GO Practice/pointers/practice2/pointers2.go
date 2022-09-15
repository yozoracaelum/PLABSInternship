package main

import "fmt"

func change(val int) {
	val = 8
}

func change_ptr(ptr *int) {
	*ptr = 8
}

func main() {
	x := 42

	change(x)
	fmt.Println(x)

	change_ptr(&x)
	fmt.Println(x)
}

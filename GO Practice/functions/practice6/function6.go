package main

import "fmt"

func swap(x, y int) (int, int) {
	return y, x
}

func main() {
	a, b := swap(42, 8)
	fmt.Println(a)
	fmt.Println(b)
}

package main

import "fmt"

func sum(x, y int) int {
	return x + y
}

func main() {
	result := sum(42, 8)
	fmt.Println(result)
}

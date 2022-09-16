package main

import "fmt"

func sum(nums ...int) {
	total := 0
	for _, v := range nums {
		total += v
	}
	fmt.Println(total)
}
func main() {
	sum(2, 4, 6)
	sum(42, 8)
	sum(1, 2, 3, 4, 5, 6)
}

package main

import (
	"fmt"
	"strings"
)

func main() {
	var isPrefix1 = strings.HasPrefix("Julian Evan", "Ju")
	fmt.Println(isPrefix1)

	var isPrefix2 = strings.HasPrefix("Julian Evan", "ju")
	fmt.Println(isPrefix2)
}

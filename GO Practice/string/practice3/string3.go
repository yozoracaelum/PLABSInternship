package main

import (
	"fmt"
	"strings"
)

func main() {
	var isSuffix1 = strings.HasSuffix("Julian Evan", "an")
	fmt.Println(isSuffix1)

	var isSuffix2 = strings.HasSuffix("Julian Evan", "An")
	fmt.Println(isSuffix2)
}

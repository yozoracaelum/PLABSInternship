package main

import (
	"fmt"
	"strconv"
)

func main() {
	var bul = true
	var str = strconv.FormatBool(bul)

	fmt.Println(str)
}

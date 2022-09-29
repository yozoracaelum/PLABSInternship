package main

import (
	"fmt"
	"regexp"
)

func main() {
	var text = "banana burger soup"
	var regex, _ = regexp.Compile(`[a-z]+`)

	var str1 = regex.FindAllString(text, -1)
	fmt.Println(str1)

	var str2 = regex.FindAllString(text, 1)
	fmt.Println(str2)
}

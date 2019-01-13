package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Print(uniqueMorseRepresentations([]string{"gin", "zen", "gig", "msg"}))
}


func uniqueMorseRepresentations(words []string) int {

	morsePatt:=[]string{".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."}

	res:= make(map[string]int)

	lengthOfWords:=len(words)
	for i:=0; i< lengthOfWords;i++  {
		var buffer bytes.Buffer
		curWord:= words[i]
		for _, letter := range curWord {
			buffer.WriteString(morsePatt[letter-97])
		}
		str:=buffer.String()
		res[str]=1
	}

	return len(res);
}

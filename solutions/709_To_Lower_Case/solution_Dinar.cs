public string ToLowerCase(string str)
{
	var charArr = str.ToCharArray();
	var len = charArr.Length;
	for (int i = 0; i < len; i++)
	{
		var val = charArr[i];
		
		if (val >= 'A' && val <= 'Z')
		{			
			charArr[i] = (char)(val + 32);
		}	
	}
	return new String(charArr);
}
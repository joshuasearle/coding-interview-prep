function longestSubstring(text: string, k: number): number {
  // Base cases
  if (k <= 1) return text.length;
  if (text.length < k) return 0;

  // Calc freq of each char in text | O(n)
  const freqs = {};
  for (let char of text) {
    if (freqs[char]) {
      freqs[char]++;
    } else {
      freqs[char] = 1;
    }
  }

  // See if text is a valid string | O(n)
  let pointer = 0;
  while (pointer < text.length && freqs[text[pointer]] >= k) {
    pointer++;
  }

  if (pointer === text.length) return text.length;

  // Test all strings split on the infrequent elements
  let maxLength = 0;
  let start = 0;
  let current = 0;

  while (current < text.length) {
    if (freqs[text[current]] < k) {
      let substring = text.slice(start, current);
      let substringLength = longestSubstring(substring, k);
      maxLength = Math.max(maxLength, substringLength);
      start = current + 1;
    }
    current++;
  }

  // Check last substring
  const lastSubstring = text.slice(start, current);
  const lastSubstringLength = longestSubstring(lastSubstring, k);
  maxLength = Math.max(maxLength, lastSubstringLength);

  // Return result
  return maxLength;
}

console.log(longestSubstring('abababcabab', 3));

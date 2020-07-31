function longestSubstring(text: string, k: number): number {
  return longestSubstringUtil(text, 0, text.length, k);
}

function longestSubstringUtil(
  text: string,
  start: number,
  end: number,
  k: number
) {
  const length = end - start;

  // Base cases
  if (k <= 1) return length;
  if (length < k) return 0;

  // Calc freq of each char in text | O(n)
  const freqs = {};
  for (let i = start; i < end; i++) {
    let char = text[i];
    if (freqs[char]) {
      freqs[char]++;
    } else {
      freqs[char] = 1;
    }
  }

  // See if text is a valid string | O(n)
  let pointer = 0;
  while (pointer < end && freqs[text[pointer]] >= k) {
    pointer++;
  }

  if (pointer === end) return length;

  // Test all strings split on the infrequent elements
  let maxLength = 0;
  let substringStart = start;
  let current = start;

  while (current < length) {
    if (freqs[text[current]] < k) {
      let substringLength = longestSubstringUtil(
        text,
        substringStart,
        current,
        k
      );
      maxLength = Math.max(maxLength, substringLength);
      substringStart = current + 1;
    }
    current++;
  }

  // Check last substring
  const lastSubstringLength = longestSubstringUtil(
    text,
    substringStart,
    current,
    k
  );
  maxLength = Math.max(maxLength, lastSubstringLength);

  // Return result
  return maxLength;
}

console.log(longestSubstring('abababcabab', 3));

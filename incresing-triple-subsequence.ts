function incresingTriplet(nums: Array<number>) {
  // Keep track of two pointers
  // Key invariant: first is always smaller than second
  let first = Infinity;
  let second = Infinity;

  for (let num of nums) {
    if (num < first) {
      // Need to check first first, to maintain invariant
      first = num;
    } else if (num < second) {
      second = num;
    } else {
      // If we find a number larger than first and second, we have found a triplet
      return true;
    }
  }
  return false;
}

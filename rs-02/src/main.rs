use std::collections::HashMap;
use std::fs;

fn main() {
    let input = fs::read_to_string("input").expect("Error reading input");
    println!("part_1 {}", part_1(&input));
    println!("part_2 {}", part_2(&input));
}

/// Counting the number that have an ID containing exactly two of any letter and then separately
/// counting those with exactly three of any letter. Then multiplying those two counts together to
/// get a rudimentary checksum
fn part_1(input: &str) -> i32 {
    let mut two_count = 0;
    let mut three_count = 0;

    for line in input.lines() {
        let frequencies = line.chars().fold(HashMap::new(), |mut acc, char| {
            *acc.entry(char).or_insert(0) += 1;
            acc
        });
        if frequencies.values().any(|&x| x == 2) {
            two_count += 1;
        }
        if frequencies.values().any(|&x| x == 3) {
            three_count += 1;
        }
    }
    two_count * three_count
}

/// find two strings with only one character difference and print their common characters
fn part_2(input: &str) -> String {
    for s1 in input.lines() {
        for s2 in input.lines() {
            let diffs = string_differences(s1, s2);
            if diffs.len() == 1 {
                let mut result = s1.to_string();
                result.remove(diffs[0]);
                return result;
            }
        }
    }
    panic!("No match found");
}

fn string_differences(s1: &str, s2: &str) -> Vec<usize> {
    let mut diff_indexes: Vec<usize> = Vec::new();
    for (i, (c1, c2)) in s1.chars().zip(s2.chars()).enumerate() {
        if c1 != c2 {
            diff_indexes.push(i);
        }
    }
    diff_indexes
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1_small() {
        let input = "abcdef\nbababc\nabbcde\nabcccd\naabcdd\nabcdee\nababab\n";
        assert_eq!(part_1(&input), 12);
    }

    #[test]
    fn test_part_1_full() {
        let input = fs::read_to_string("input").expect("Error reading input");
        assert_eq!(part_1(&input), 6000);
    }

    #[test]
    fn test_string_differences() {
        assert_eq!(string_differences("abcde", "axcye"), vec![1, 3]);
        assert_eq!(string_differences("fghij", "fguij"), vec![2]);
    }

    #[test]
    fn test_part_2_small() {
        let input = "abcde\nfghij\nklmno\npqrst\nfguij\naxcye\nwvxyz\n";
        assert_eq!(part_2(&input), "fgij");
    }

    #[test]
    fn test_part_2_full() {
        let input = fs::read_to_string("input").expect("Error reading input");
        assert_eq!(part_2(&input), "pbykrmjmizwhxlqnasfgtycdv");
    }
}

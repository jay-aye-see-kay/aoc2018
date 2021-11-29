use std::fs;
use std::collections::HashSet;

fn main() {
    let input = fs::read_to_string("input.txt").expect("Error reading input.txt");
    println!("part 1: {}", part_1(&input));
    println!("part 2: {}", part_2(&input));
}

/// Starting with a frequency of zero, what is the resulting frequency after all of the changes in
/// frequency have been applied?
fn part_1(input: &str) -> i32 {
    let mut sum = 0;
    for line in input.lines() {
        let val = line.parse::<i32>().unwrap();
        sum += val;
    }
    return sum;
}


/// find the first frequency it reaches twice
fn part_2(input: &str) -> i32 {
    let mut sum = 0;
    let mut seen = HashSet::new();

    loop {
        for line in input.lines() {
            let val = line.parse::<i32>().unwrap();
            sum += val;
            if seen.contains(&sum) {
                return sum;
            }
            seen.insert(sum);
        }
    }
}

// tests
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        let input = "+1\n-2\n+3\n+1\n";
        assert_eq!(part_1(input), 3);
    }

    #[test]
    fn test_part_2() {
        let input = "+1\n-2\n+3\n+1\n";
        assert_eq!(part_2(input), 2);
    }
}

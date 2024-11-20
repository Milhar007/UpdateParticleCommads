import re

def convert_particle_line(line):
    # Skip lines already in the new format
    if "minecraft:dust{" in line:
        return line  # Return as-is if already converted

    # Match the old particle line format
    match = re.match(
        r'particle minecraft:dust (?P<r>\d+(\.\d+)?) (?P<g>\d+(\.\d+)?) (?P<b>\d+(\.\d+)?) (?P<scale>\d+(\.\d+)?) (?P<rest>.+)',
        line
    )
    if match:
        # Convert to float to ensure 0 becomes 0.0 and format as floating-point
        r = f"{float(match.group('r')):.1f}"
        g = f"{float(match.group('g')):.1f}"
        b = f"{float(match.group('b')):.1f}"
        scale = f"{float(match.group('scale')):.1f}"
        rest = match.group('rest')
        
        # Use an f-string for formatting
        return f"particle minecraft:dust{{color:[{r},{g},{b}],scale:{scale}}} {rest}"
    else:
        # If the line does not match the pattern, return as-is
        return line

def convert_particle_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            line = line.strip()  # Remove trailing whitespace
            converted_line = convert_particle_line(line)
            outfile.write(converted_line + '\n')

if __name__ == "__main__":
    # Input and output file names
    input_file = "particles.txt"  # Input file with particle commands
    output_file = "converted_particles.txt"  # Output file for converted commands

    # Run the conversion
    convert_particle_file(input_file, output_file)
    print(f"Converted particle commands saved to {output_file}")

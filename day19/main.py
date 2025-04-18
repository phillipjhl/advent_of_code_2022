"""
Author - Phillip Langland

This script reads the local prompt.txt file, and calculates the "level of quality" of all the blueprints provided in that file which it will print out in the console.

"""

RULE_MAPPINGS: list = ["ORE", "CLAY", "OBSIDIAN", "GEODE"]

def main():
    global RULE_MAPPINGS
    # read the blueprints line by line
    with open('prompt.txt', 'r') as prompt_file:
        for line in prompt_file:
            calculate_bp_quality(line)

def calculate_bp_quality(line: str):
    QUALITY = 0
    ORE_AMT = 0
    CLAY_AMT = 0
    OBSIDIAN_AMT = 0
    GEODE_AMT = 0
    ORE_ROBOTS = 0
    CLAY_ROBOTS = 0
    OBSIDIAN_ROBOTS = 0
    GEODE_ROBOTS = 0

    line = line.strip()
    blueprint_tuple = line.split(":")
    
    print('{0}:'.format(blueprint_tuple[0]))
    print("---------------------------------------------\n")
    blueprint_rules = blueprint_tuple[1].split(".")
    blueprint_rules.pop()

    build_instructions = create_build_instructions(blueprint_rules)

    print('BUILD INSTRUCTIONS: {0}\n'.format(build_instructions))

    # for i in range(len(24)):


    # TO DO: calculate the max number of geodes a blueprint can build over 24 minutes. 
    # Each robot can collect 1 of its resource type per minute. 
    # It also takes one minute for the robot factory (also conveniently from your pack) to construct any type of robot, 
    # although it consumes the necessary resources available when construction begins. 


def create_build_instructions(rules: list):
    cost_mapping_dict = {}

    # map rules
    for i in range(len(rules)):
        rule = rules[i]
        instruction = rule.strip()

        # split on multiple instructions
        instruction = instruction.split("and")

        # if there are multiple instructions, we need to separate them out 
        if len(instruction) > 0:
            ore_cost = instruction[0].split("costs")[-1]
            instruction[0] = ore_cost
            
            # for each cost, strip unwanted whitespace
            instruction = strip_whitespaces(instruction)
            
        # need to make instruction list a dictionary
        material_dict = build_material_dict(instruction)

        # add cleaned up intructions to result dict to make output all instructions
        cost_mapping_dict[RULE_MAPPINGS[i]] = material_dict

    return cost_mapping_dict

def build_material_dict(materials_list: list):
    """
    Takes a list of materials and takes the material name to use as a key, and the count to use as a value

    Returns the result dictionary.

    """
    material_dict = {}
    for i in range(len(materials_list)):
        material = materials_list[i]
        count_material_tuple = material.split(" ")
        count = count_material_tuple[0]
        material = count_material_tuple[1].upper()

        material_dict[material] = count

    return material_dict

def strip_whitespaces(list: list):
    """
    Strip whitespaces for all elements in a list, and return the result
    """
    stripped_list = []

    for i in range(len(list)):
        item = list[i]
        stripped_list.append(item.strip())

    return stripped_list

if __name__ == "__main__":
    main()
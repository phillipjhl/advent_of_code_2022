RULE_MAPPINGS: list = ["ORE", "CLAY", "OBSIDIAN", "GEODE"]


def main():
    global RULE_MAPPINGS
    # read the blueprints line by line
    with open('prompt.txt', 'r') as prompt_file:
        for line in prompt_file:
            get_blueprint_config(line)

# Return
def get_blueprint_config(line: str):
    line = line.strip()
    print('BLUEPRINT: {0}'.format(line))
    blueprint_tuple = line.split(":")
    
    blueprint_rules = blueprint_tuple[1].split(".")
    blueprint_rules.pop()

    build_instructions = create_rules(blueprint_rules)

    print(build_instructions)


def create_rules(rules: list):
    cost_mapping_dict = {}

    # map rules
    for i in range(len(rules)):
        rule = rules[i]
        clean_rule = rule.strip()
        clean_rule = clean_rule.split("and")
        # if there are multiple instructions, splite them
        if len(clean_rule) > 0:
            ore_cost = clean_rule[0].split("costs")[-1].strip()
            clean_rule[0] = ore_cost 

        cost_mapping_dict[RULE_MAPPINGS[i]] = clean_rule

    return cost_mapping_dict

if __name__ == "__main__":
    main()
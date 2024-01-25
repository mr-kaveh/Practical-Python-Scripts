# Filter genetic Data using python sets
# Filtering genetic data typically involves selecting specific elements that 
# meet certain criteria from a set of genetic information. Here's a simple example code 
# that demonstrates filtering genetic data using Python sets. In this example
# we'll assume that the genetic data is represented by sets of genes:

def filter_genetic_data(genetic_data, filter_criteria):
    filtered_data = {individual: genes & filter_criteria for individual, genes in genetic_data.items()}
    return filtered_data

# Example usage:
genetic_data = {
    'Individual1': {'GeneA', 'GeneB', 'GeneC'},
    'Individual2': {'GeneB', 'GeneD', 'GeneE'},
    'Individual3': {'GeneA', 'GeneC', 'GeneF'}
}

filter_criteria = {'GeneA', 'GeneC'}

filtered_genetic_data = filter_genetic_data(genetic_data, filter_criteria)

# Display the filtered genetic data
for individual, genes in filtered_genetic_data.items():
    print(f"{individual}: {genes}")

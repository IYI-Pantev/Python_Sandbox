import pandas

data = pandas.read_csv("50_states.csv")
# print(data)

all_states = data.state.to_list()
print(all_states)

state_data = data[data.state == "Ohio"]
print(state_data)
print(state_data.x)
# Function to join given bound_by and tag
def join_middle(bound_by, tag_name):
  # complete the statement below to return the string as required
  return bound_by[0 :int(len(bound_by)/2)   ] + tag_name + bound_by[int(len(bound_by)/2):  ]
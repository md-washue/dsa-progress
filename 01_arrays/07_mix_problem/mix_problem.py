def route_moved_backward(disances):
    for i in range(1, len(distances)):
            if distances[i] < distances[i - 1]:
                return True
    
    return False
distances = [2, 5,3,7,8,4,9]





print(route_moved_backward(distances))

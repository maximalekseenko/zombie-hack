import connections
import world


connections.Init()
print(connections.PutIntoQueue())

world.__worldStatic = connections.GetWorldStatic()
world.__worldDynamic = connections.GetWorldDynamic()

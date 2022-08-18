from autobahn.asyncio.component import Component, run
import os


url = "ws://0.0.0.0:8989/public"
realmv = "ami"
print(url, realmv)
component = Component(transports=url, realm=realmv)


@component.on_join
async def joined(session, details):
    print("session ready")
    try:
        res = await session.call('get_lighting_type_list')
        print("\ncall result: {}\n".format(res))
    except Exception as e:
        print("call error: {0}".format(e))
    await session.leave()


if __name__ == "__main__":
    run([component])        




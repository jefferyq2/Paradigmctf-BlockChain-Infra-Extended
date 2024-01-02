import json
from pathlib import Path

import eth_sandbox
from web3 import Web3


def deploy(web3: Web3, deployer_address: str, player_address: str) -> str:
    rcpt = eth_sandbox.sendTransaction(web3, {
        "from": deployer_address,
        "value": Web3.toWei(100, 'ether'), # our Setup contract expects 100 ether. So let's give it 100 ether.
        "data": json.loads(Path("compiled/Setup.sol/Setup.json").read_text())["bytecode"]["object"],
    })

    return rcpt.contractAddress

app = eth_sandbox.run_launcher(deploy)

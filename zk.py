import wallet
import chain
import pickle
import object


if "__main__" == __name__:
    C = chain.load_chain('chain/chain.pickle')
    if C is None:
        C = chain.Chain()
    chain.save_chain(C, 'chain/chain.pickle')
    print('\nSTART\n')
    C, W1 = wallet.create_or_load_wallet(C, "wallets/wallet_A.pickle")
    C, W2 = wallet.create_or_load_wallet(C, "wallets/wallet_B.pickle")

    print('Block:', C.block_number)
    W2 = C.add_object_to_chain(W2)
    wallet.save_wallet(W1, "wallets/wallet_A.pickle")
    wallet.save_wallet(W2, "wallets/wallet_B.pickle")
    C.print_and_update()
    chain.save_chain(C, 'chain/chain.pickle')
    
    print('Block:', C.block_number)
    C, W1, W2 = wallet.trade(C, W2, W1, W2.objs[0])
    wallet.save_wallet(W1, "wallets/wallet_A.pickle")
    wallet.save_wallet(W2, "wallets/wallet_B.pickle")
    C.print_and_update()
    chain.save_chain(C, 'chain/chain.pickle')
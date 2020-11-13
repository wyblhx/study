from deal_dump.dump import Dump

deal=Dump('dump.test')
#print(deal.atoms_number,deal.boxl[0])
#deal.read_snapshots()
deal.get_one_snapshot(deal.frame)
#print(deal.atoms_number,deal.frame)

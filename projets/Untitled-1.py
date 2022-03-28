class CompteBancaire:
  def __init__(self,num,solde,prenom,nom):
      self.num=num
      self.solde=solde
      self.prenom=prenom
      self.nom=nom
  def getNum(self):
    return self.num
  def setNum(self,num):
    self.num=num
  def getSolde(self):
    return self.solde
  def setSolde(self,solde):
    self.solde=solde
  def getPrenom(self):
    return self.prenom
  def setPrenom(self,prenom):
    self.num=prenom
  def getNom(self):
    return self.nom
  def setNom(self,nom):
    self.num=nom
  def affiche(self):
    print("le numero",self.num,"solde",self.solde,"est",self.prenom,self.nom)

class CompteCourant(CompteBancaire):
  def __init__(self, num, solde, prenom, nom,libele):
      super().__init__(num, solde, prenom, nom)
      self.libele=libele
  def retrait(self,montant):
    if montant <= getSolde:
      print("Operation reussie")
      solde= getSolde-montant
    else:
      print("solde insuffisant")
  def depot(self,montant):
    self.solde=self.solde+montant
    print("Operation reussie") 

  mor=CompteBancaire(1,10000,'mor','diouf')
  print(mor.affiche())
  cour=CompteCourant(1,10000,'mor','diouf','md')
  print(cour.retrait(5000))
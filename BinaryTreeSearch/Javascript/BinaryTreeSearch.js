// Node class
class Node{
   constructor(data){
    this.data = data;
    this.right = null;
    this.left = null;
   }
}// fin class node
class Binarytreesearch{
   constructor(){
    this.root = null;
   }
   insert(data){
    var newNode = new Node(data);
    if(this.root === null)
      {
       this.root = newNode;
       console.log("father root : " + " " + this.root.data);
      }
    else
       this.insertNode(this.root,newNode);
   } // fin insert
   insertNode(node,newNode){
    if(node.data > newNode.data){
       if(node.left === null){
          node.left = newNode;
          console.log("On fait la recherche a gauche");
          console.log("father : " + " " + node.data + " " + "Left son : " + " " +node.left.data );
       }
       else
         this.insertNode(node.left,newNode);
    }
    else{
       if(node.right === null){
          node.right = newNode;
          console.log("On fait la recherche a droite");
          console.log("father : " + " " + node.data + " " + "right son : " + " " +node.right.data );
       }
       else
         this.insertNode(node.right,newNode);
    }
   } // fin isertNode
}// fon classe arbre binaire
var x = new Binarytreesearch();
    x.insert(10);
    x.insert(8);
    x.insert(15);
    x.insert(9);
    x.insert(7);
    x.insert(17);
    x.insert(14);
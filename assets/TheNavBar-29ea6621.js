import{d as o,z as i,o as t,c as _,f as n,n as l,_ as c,r as u,k as f,A as s}from"./index-12433a3f.js";const v=["size"],p=o({__name:"TheIcon",props:{icon:null,size:null},setup(e){return i(a=>({c4a7bd64:e.size+"px"})),(a,r)=>(t(),_("div",null,[n("span",{class:l(["icon iconfont",e.icon]),size:e.size},null,10,v)]))}});const I=c(p,[["__scopeId","data-v-dc8d3f8b"]]),m=o({__name:"TheAvatar",props:{size:null,src:null,isCommentContent:{type:Boolean,default:()=>!1}},setup(e){return(a,r)=>{const d=u("el-avatar");return t(),f(d,{class:l(["avatar",{commentAvatar:e.isCommentContent}]),shape:"circle",size:e.size,src:e.src},null,8,["class","size","src"])}}});const $=c(m,[["__scopeId","data-v-81c11ba5"]]);const h={},z={class:"flex flexJustifySpaceBetween nav"},x={class:"flex"},T={class:"group"},y={class:"flex"};function B(e,a){return t(),_("nav",z,[n("div",x,[s(e.$slots,"avatarAndNickname",{},void 0,!0)]),n("div",T,[s(e.$slots,"input",{},void 0,!0)]),n("div",y,[s(e.$slots,"postIcon",{},void 0,!0),s(e.$slots,"dropDown",{},void 0,!0)])])}const b=c(h,[["render",B],["__scopeId","data-v-d9cf1fa0"]]);export{$ as T,I as a,b};

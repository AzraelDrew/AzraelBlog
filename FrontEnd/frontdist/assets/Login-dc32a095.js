import{d as x,u as g,i as d,b as v,r as h,o as w,c as y,g as s,l as B,f as e,x as V,T as E,E as i,p as S,q as k,_ as C}from"./index-734f478a.js";import{T as p}from"./TheButton-6961f5fb.js";const _=o=>(S("data-v-4e0516e6"),o=o(),k(),o),I={class:"flex flexWarp loginBox"},K=["onKeydown"],L=_(()=>e("div",{class:"flex"},[e("h1",null,"AzraelBlog")],-1)),T={class:"inputBox"},b={class:"inputBox"},N=_(()=>e("div",{class:"flex flexJustifyEnd",style:{"margin-top":"10px"}},[e("a",{class:"forgetPwd link",href:""},"忘记密码?")],-1)),U={class:"flex inputBox flexJustifySpaceBetween"},J=x({__name:"Login",setup(o){const f=g(),l=d(""),n=d(""),m=v();async function c(){let t=await f.userLogin(l.value,n.value);if(t=="pwderr"){i({title:"Error",message:"密码错误",type:"error"});return}else if(t=="none"){i({title:"Error",message:"用户不存在",type:"error"});return}t=="OK"&&(console.log(`%c
       ███████╗██╗   ██╗ ██████╗ ██████╗███████╗███████╗███████╗██╗
       ██╔════╝██║   ██║██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝██║
       ███████╗██║   ██║██║     ██║     █████╗  ███████╗███████╗██║
       ╚════██║██║   ██║██║     ██║     ██╔══╝  ╚════██║╚════██║╚═╝
       ███████║╚██████╔╝╚██████╗╚██████╗███████╗███████║███████║██╗
       ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝╚══════╝╚══════╝╚══════╝╚═╝
    `,"color:#7c9beb"),i({title:"Success",message:"登录成功",type:"success",duration:1e3}),m.replace({name:"Home"}))}return(t,a)=>{const u=h("el-input");return w(),y("div",I,[s(E,{name:"fade",appear:""},{default:B(()=>[e("div",{class:"felx login",onKeydown:V(c,["enter"])},[L,e("div",T,[s(u,{modelValue:l.value,"onUpdate:modelValue":a[0]||(a[0]=r=>l.value=r),class:"input",placeholder:"用户名"},null,8,["modelValue"])]),e("div",b,[s(u,{modelValue:n.value,"onUpdate:modelValue":a[1]||(a[1]=r=>n.value=r),class:"input",type:"password",placeholder:"密码","show-password":!0},null,8,["modelValue"]),N]),e("div",U,[s(p,{class:"loginButton",text:"注册"}),s(p,{class:"loginButton",text:"登录",onClick:c})])],40,K)]),_:1})])}}});const A=C(J,[["__scopeId","data-v-4e0516e6"]]);export{A as default};

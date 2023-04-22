import{d as y,b as A,J as B,u as S,a as T,i as n,r as _,o as U,k as D,l as E,f as r,L as v,M as f,g as o,T as F,E as I,_ as P}from"./index-734f478a.js";import{T as h}from"./TheButton-6961f5fb.js";const J={class:"container editArticle"},N={class:"flex flexJustifySpaceBetween"},R={class:"flex flexJustifyEnd cancelPost"},j=y({__name:"PostArticle",setup(q){const g=`::: tip
  你可以点击 toolbar 中的 tip 来快速插入
:::

::: warning
  这是一段警告
:::

::: danger
  这是一个危险警告
:::

::: details
  这是一个详情块，在 IE / Edge 中不生效
:::

::: tip 自定义标题
  你也可以自定义块中的标题
:::

::: danger STOP
  危险区域，禁止通行
:::

`,p=A();B();const x=S(),m=T(),i=n(g),u=n(""),d=n(""),l=n(!1);function b(t,e,s){let c=s[0],a=new FormData;a.append("imgnode",c),m.post("api/article/img/",a).then(C=>{e({url:C.data.url,desc:"在这里插入图片描述"})})}function V(){l.value=!l.value}function k(){p.push({name:"Home"})}async function w(){let t=new FormData;t.append("token",x.userInfo.token),t.append("title",u.value),t.append("describe",d.value),t.append("content",i.value),t.append("cover","");let e=await m.post("api/add/article/",t);console.log(e),I({title:"Success",message:"发布成功",type:"success"}),p.push({name:"ViewArticle",params:{id:e.data.id}})}return(t,e)=>{const s=_("el-input"),c=_("v-md-editor");return U(),D(F,{name:"fade",appear:""},{default:E(()=>[r("div",J,[v(r("div",N,[o(s,{modelValue:u.value,"onUpdate:modelValue":e[0]||(e[0]=a=>u.value=a),class:"input",placeholder:"标题..."},null,8,["modelValue"]),o(s,{modelValue:d.value,"onUpdate:modelValue":e[1]||(e[1]=a=>d.value=a),class:"input",placeholder:"描述..."},null,8,["modelValue"])],512),[[f,!l.value]]),o(c,{class:"md","left-toolbar":"undo redo clear | h bold italic strikethrough quote | emoji todo-list | ul ol table hr | link image code | save",modelValue:i.value,"onUpdate:modelValue":e[2]||(e[2]=a=>i.value=a),autofocus:!0,onFullscreenChange:V,"disabled-menus":[],onUploadImage:b,height:"76vh"},null,8,["modelValue"]),v(r("div",R,[o(h,{text:"取消",onClick:k,class:"button cancelButton"}),o(h,{text:"发布",onClick:w,class:"button"})],512),[[f,!l.value]])])]),_:1})}}});const M=P(j,[["__scopeId","data-v-49e7b15c"]]);export{M as default};

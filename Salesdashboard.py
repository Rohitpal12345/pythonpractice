import streamlit as st

st.set_page_config(page_title="Sales Dashboard",layout="wide")
st.title("Sales Dashboard")
st.caption("Showing The Details of Sales")

   # Taking variable to store products
products=[
    {"Product":"Laptop","Brand":"HP","Sales":50000},
    {"Product":"Phone","Brand":"SAMSUNG", "Sales":20000},
    {"Product":"Shoes","Brand":"CAMPUS","Sales":10000},
    {"Product":"Radio","Brand":"MURFI","Sales":5000},
    {"Product":"Led TV","Brand":"TCL","Sales":40000},
    {"Product":"Air-Conditioner","Brand":"VOLTAS","Sales":80000},
    ]

#use sidebar
st.sidebar.title("🧾Menu")
page=st.sidebar.radio("Navigate",["🏡Dashboard","📦Product","🗄️Reports","⚙️Settings"])

if page=="🏡Dashboard":
    col1,col2,col3=st.columns(3)
    with col1:
          st.metric("Total Sales","3,50,000")
    with col2:
          st.metric("Total Orders","130")
    with col3: 
          st.metric("Profit","50,000") 


st.subheader("Select Region")
region=st.selectbox("Region",["North","South","East","West"])
st.write("Selected Region",region)

if st.button("Refresh"):
     st.success("Dasboard Refreshed!")
     st.progress(80)

 
     

elif page=="📦Product":
     st.title("📦Product")
     st.write("Product detail will be shown here")
     st.dataframe(products)
# show all product in a table by using dataframe

    

elif page=="🗄️Reports":
     st.title("🗄️Reports")
     st.write("Reports will be shown here")
     st.subheader("🗄️Sales Reports")
     # Total sale add krna
     total_sales=sum(i["Sales"] for i in products)
     st.metric("Total Product Sale",total_sales)
     st.subheader("Product Wise Report")
     st.dataframe(products)
     st.subheader("Heighest Selling Product")
     heighest=max(products,key=lambda x:x["Sales"])
     st.success(f"🏆{heighest['Product']}-Sales{heighest['Sales']}")
     

elif page=="⚙️Settings":
     st.title("⚙️Settings")
     st.write("Setting Page")
     st.subheader("Dashboard Settings")
     #theme option
     theme=st.selectbox("Choose Theme",["Light","Dark"])
     st.write("Selected Theme",theme)
     #Notification Settings
     notification=st.checkbox("Enables Notification")
     if notification:
          st.success("Notification Enabled✅")
     else:
          st.warning("Notification Disabled")


    # username
     username=st.text_input("Enter UserName")
     if username: 
          st.info(f"Welcome:{username}👋")


    #save button
if st.button("Save Settings"): 
     st.success("Setting Save Successfully✅")   
     pass



search=st.text_input("🔍Search Product")
found=False

for i in products:
    if search.lower() in i["Product"].lower():
        st.write(i)
        found=True
        st.write("✅ available")
       
if found==False:
       st.error("Product unavailable. Please check the product name and try again.")

        
pass
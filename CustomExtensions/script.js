tableau.extensions.initializeAsync().then(() => {

    document.getElementById("status").innerHTML =
        "Connected to Tableau";

});

document.getElementById("applyBtn").onclick = async function(){

    const dashboard =
        tableau.extensions.dashboardContent.dashboard;

    const worksheet =
        dashboard.worksheets[0];

    const region =
        document.getElementById("region").value;

    await worksheet.applyFilterAsync(

        "Region",

        [region],

        tableau.FilterUpdateType.Replace

    );

};
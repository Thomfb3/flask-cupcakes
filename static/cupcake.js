function updateRangeInput(val) {
    $('#cupcake-range-value').text(val);
}


$('#cupcake-table').click(function (e) {
    const id = e.target.getAttribute("data-btn-id");
    $('#cupcake-delete-btn').attr("data-id", `${id}`)

    $('#modal-message').text(`Are you sure you want to delete cupcake ${id} ?`)
});



/////////Create cupcake 
$('#cupcake-create-btn').click(createCupcake);


async function createCupcake(e) {
    e.preventDefault();

    let flavor = $('#flavor').val();
    let size = $('#size').val();
    let image = $('#image').val();
    let rating = $('#rating').val();

    params = { "flavor": flavor, "size": size, "image": image, "rating": rating }

    await axios.post(`api/cupcakes`, params)

    location.href = "http://127.0.0.1:5000/";

}


/////////Update cupcake 
$('#cupcake-update-btn').click(updateCupcake);


async function updateCupcake(e) {
    e.preventDefault();

    const id = e.target.getAttribute("data-id");

    let flavor = $('#flavor').val();
    let size = $('#size').val();
    let image = $('#image').val();
    let rating = $('#rating').val();

    params = { "flavor": flavor, "size": size, "image": image, "rating": rating }
 
    await axios.patch(`http://127.0.0.1:5000/api/cupcakes/${id}`, params)

    location.href = "http://127.0.0.1:5000/";

}



/////////Delete cupcake 
$('#cupcake-delete-btn').click(deleteCupcake);



async function deleteCupcake() {
    const id = $('#cupcake-delete-btn').attr("data-id");
    await axios.delete(`api/cupcakes/${id}`)

    const tableCupcake = $(`[data-btn-id=${id}]`)
    tableCupcake.parent().parent().remove()
}




from routes import app, warehouse, order_manager


if __name__ == '__main__':
    # SIGINT to stop (Ctrl + C)
    app.run(debug=True)

    # Saves the data
    print('Saving...')
    warehouse.save_data()
    order_manager.save_data()
    print('Save complete')